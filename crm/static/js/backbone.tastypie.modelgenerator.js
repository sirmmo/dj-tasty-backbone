/*
* Backbone-tastypie model generator
* Created by Marco Montanari
* released under 3 clause BSD 
*/

(function( undefined ) {

    Backbone.SchemaUrl = "";
	Backbone.LoadModelsFromUrl = function(url, models){
		Backbone.SchemaUrl =url;
		$.getJSON(Backbone.SchemaUrl , function(data){
			Backbone.LoadModels(data, models)
		});
	}

	Backbone.LoadModels = function(object, models){
		for (var model in object){
			var _mdl = {};
			_mdl['name'] = Backbone.ModelNameGenerator (model);
			_mdl['url'] = object[model]['list_endpoint'].slice(0,-1);
			_mdl['container_name'] = Backbone.ModelNameGenerator (model)+"Container";
    		_mdl['schema_url'] = object[model]['schema'];
            
            _mdl['validator'] = {};
            _mdl['schema'] = {};
            
			
			$.getJSON(_mdl['schema_url'] , function(data){
				for (var field in data['fields']){
					_mdl['validator'][field] = {};
                    _mdl['validator'][field]['type'] = data['fields']['type'];
                    if (data['fields']['blank'] == false)
                        _mdl['validator'][field]['required'] = true;
                    if (data['fields']['extras'] != null)
                        _mdl.schema[field] = data['fields'][field]['extras'];
                    else
                        _mdl.schema[field] = {};
				}
			});
            
            window[_mdl['name']] = Backbone.Model.extend({
				urlRoot: _mdl['url'],
                validate:_mdl['validator']
                if schema
			});
			window[_mdl['container_name']] = Backbone.Collection.extend({
				urlRoot: _mdl['url'], 
				model: window[_mdl['name']]
			});
		}
	}
	
	Backbone.ModelNameGenerator = function (string)
	{
    	return string.charAt(0).toUpperCase() + string.slice(1);
	}


})();