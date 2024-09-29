$(document).ready(function(){
    function toggleNav() {
      var screenWidth = $(window).width();
      
      if(screenWidth <= 691){
        $(".nav-links").hide();  
        $(".burger").off("click").on("click", function(){
          $(".nav-links").toggle();
        });
      } else {
        $(".nav-links").show();  
        $(".burger").off("click");  
      }
    }
  
    toggleNav();   
    $(window).resize(toggleNav);  
  });
  