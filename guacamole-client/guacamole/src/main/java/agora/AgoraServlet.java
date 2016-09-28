package agora;

import java.io.IOException;
import javax.servlet.ServletException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.util.*;
import java.io.*;
import java.nio.file.*;
import java.nio.charset.*;
import java.lang.Thread;

/**
 * Servlet implementation class AgoraServlet
 */

public class AgoraServlet extends HttpServlet {
 private static final long serialVersionUID = 1L;

    
    public AgoraServlet() {
       
    }

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	// Need some way to differentiate between program name and program path (e.g. "mario-cart" vs "108/108-final-examples/mario-cart/main.py"), but they could be the same.

	// Hashtable to hardcode the python version for each available program.  Eventually in
        // an "upload" page interface, it could even be a radio button to choose python 2 or 3.
	HashMap<String, String> programs;
	programs = new HashMap<String, String>();
	programs.put("distrib.py", "2");
	programs.put("tkintertest2.py", "3");
	programs.put("mario-cart", "3");

    	String progName = request.getParameter("program");
	String langVersion = programs.get(progName);
	System.out.println("Language version is " + langVersion);

	// Run start.sh script to start the vnc server with a python program and version
	Process P2 = new ProcessBuilder().inheritIO().command("/home/Agora/start.sh" , progName, langVersion).start();
	//name += "   Running start.sh... program name is " + progName;
	System.out.println("This is Corwin console output from Agora Servlet");

	// Read from the file /home/Agora/pids/recent.txt - which contains the most recently started process.  Use a delay 
	// to make sure the file has already been written to by start.sh when we read it.
	// maybe also remove the delay in the angular reload
	try {
		System.out.println("about to sleep for 0.5 seconds");
		Thread.sleep(500);
	} catch(InterruptedException ex) {
		Thread.currentThread().interrupt();
	}
	List<String> lines = Files.readAllLines(Paths.get("/home/Agora/pids/recent.txt"), StandardCharsets.US_ASCII);
	String myPid = lines.get(0);
	System.out.println("the most recent pid is " + myPid);

   
    response.setContentType("text/plain");  
    response.setCharacterEncoding("UTF-8"); 
    response.getWriter().write(myPid); 


  }

  
 protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

  
 }

}
