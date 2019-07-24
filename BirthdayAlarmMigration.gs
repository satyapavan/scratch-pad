var META_DATA = [
  ['Name ', 'email_id', 'January 1' ]
];

function migrate() {

  for(row=0; row < META_DATA.length; row++) {
    var name  = META_DATA[row][0];
    var email = META_DATA[row][1];
    var dob   = META_DATA[row][2];
    
    var Objdesc = 'name: ' + name + '\n' + 'email: ' + email + '\n' + 'DOB: ' + dob ;
    
   // console.log(dob, new Date(dob));
    
    var dob_arr = dob.split(' ');
    console.log(dob_arr.length);
    var Oyear = (dob_arr.length == 3) ? dob_arr[2] : '2019' ;
    var Omonth = dob_arr[0];
    
    // at times there could be a ',' after date, espically if there is an year associated
    var Oday = dob_arr[1].split(',')[0];
      
    var newDOB = Omonth + ' ' + Oday + ', ' + Oyear + " 00:00:00";
    
    console.log("DOB", dob, newDOB);
    
    // Creates an event series for 80 yrs
    var eventSeries = CalendarApp.getCalendarsByName("Remainders")[0].createAllDayEventSeries(
      name + ' Birthday' + ( (dob_arr.length == 3) ? ' (' + dob_arr[2] + ')' : '' ),
      new Date(newDOB),
        CalendarApp.newRecurrence().addYearlyRule()
        .times(80),
          {description: Objdesc});
    
    Logger.log('Event Series ID: ' + eventSeries.getId());
        
    }
}
