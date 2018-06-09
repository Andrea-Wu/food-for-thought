function countdown(secs){
    //if secs already 0, Jinja2/Flask will handle things
    console.log("this works")
    
    if(secs == 0){
        console.log("seconds is 0, termnating js")
        return;
    }
    
    setInterval(function(){

        //converts total seconds to seconds/minutes/hours, then displays it 
        var display_hrs = Math.floor(secs / 3600);
        secs = secs % 3600

        var display_min = Math.floor(secs / 60);

        var display_secs = secs % 60;

        document.getElementById("display_hrs").innerHTML = display_hrs;
        document.getElementById("display_min").innerHTML = display_min;
        document.getElementById("display_secs").innerHTML = display_secs;

        secs = secs -1;

        if(secs == 0){
            clearInterval(); //break from loop
        }

    },1000); //update every second

    //display the "button"
    document.getElementById("req_button").style.display = "block";
    

} 


