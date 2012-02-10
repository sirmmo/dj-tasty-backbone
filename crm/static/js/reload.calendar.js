Reload.Calendar = {};

Reload.Calendar.evtsources = [];
Reload.Calendar.selected_users = [user];
Reload.Calendar.selected_projects = [];

Reload.Calendar.ES_from_user. = function(user, pe, projects){
	if (projects.length == 0)
		return {
			url:'/tasks/'+user+'/'+pe+'/calendar.json',
			type:'GET',
			error:function (){
				alert('errore');
			}
		}
	else
		return {
			url:'/tasks/'+user+'/'+pe+'/calendar.json',
			data:{
				projects:projects
			},
			type:'GET',
			error:function (){
				alert('errore');
			}
		}
};

Reload.Calendar.reset_calendar = function (e){
	for(var el in Reload.Calendar.evtsources){
		$('#calendar').fullCalendar( 'removeEventSource', Reload.Calendar.evtsources[el] );
	}
	Reload.Calendar.evtsources = [];
	$('#calendar').fullCalendar( 'removeEvents' );
}

Reload.Calendar.add_calendars = function (){
	var pe = $('input.cal_view_sel:checked').val();
	for (ui in Reload.Calendar.selected_users){
		Reload.Calendar.add_calendar($.selected_users[ui], pe, Reload.Calendar.selected_projects);
	}
}

Reload.Calendar.add_calendar = function (user, pe, projs){
                Reload.Calendar.evtsources.push(Reload.Calendar.ES_from_user(user, pe, projs));
                $('#calendar').fullCalendar('addEventSource',Reload.Calendar.ES_from_user(user, pe, projs));
        }

Reload.Calendar.reload_calendar = function (){
                $('#calendar').fullCalendar( 'refetchEvents' );
        }

Reload.Calendar.resize = function(){
                $('#sidebar').height($(window).height()-$('header').height());
                $('#content').height($(window).height()-$('header').height());

                $('#content').width($(window).width()-$('#sidebar').width()-7);

                $('#movable').height($('#content').height()-$('#toolbar').height()-12);
                $('#movable').width($('#content').width()-7);

                $('#projects_bar').height(($('#sidebar').height()/2)-2);
                $('#users_bar').height(($('#sidebar').height()/2)-2);

                $('#calendar').fullCalendar('option', 'aspectRatio', $('#movable').width()/$('#movable').height()/0.8);
        }

Reload.Calendar.ISODateString = function(d){
		function pad(m){
			n = Math.abs(m);
			return n<10 ? '0'+n : n}
		var hours = -d.getTimezoneOffset() / 60;
                var mins = -d.getTimezoneOffset() % 60;
		var iso = d.getUTCFullYear()+'-'
			+ pad(d.getUTCMonth()+1)+'-'
			+ pad(d.getUTCDate())+'T'
			+ pad((d.getUTCHours()+hours)%24)+':'
			+ pad(d.getUTCMinutes()+mins)+':'
			+ pad(d.getUTCSeconds())+ '';
			
		return iso;
	}       


	Reload.Calendar.OnHourShowCallback = function (hour) {
		if ((hour > 17) || (hour < 9)) {
			return false; // not valid
		}
		return true; // valid
	}

	Reload.Calendar.OnMinuteShowCallback = function(hour, minute) {
 		if ((hour == 17) && (minute > 30)) { return false; } // not valid
		if ((hour == 9) && (minute < 30)) { return false; }   // not valid
		return true;  // valid
	}

