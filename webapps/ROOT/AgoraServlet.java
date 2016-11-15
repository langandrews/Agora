package ajaxagora

import java.io.IOException;
import javax.servlet.ServletException;

import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class AgoraServlet
 */
@WebServlet("/Servlets/*")
public class AgoraServlet extends HttpServlet {
 private static final long serialVersionUID = 1L;

    
    public AgoraServlet() {
       
    }

  @Override
  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    String name="hello hello";
    response.setContentType("text/plain");  
    response.setCharacterEncoding("UTF-8"); 
    response.getWriter().write(name); 
  }

  
 protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

  
 }

}
