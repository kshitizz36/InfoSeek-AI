function checkEnvironment(): { 
     try { 
         // Check the environment 
         if (process.env.NODE_ENV !== 'production') { 
             console.log('Development environment detected.'); 
         } 
     } catch (error) { 
         // Log the error and prevent app crash 
         console.error('Error checking environment:', error); 
         process.exit(1); 
     } 
 }