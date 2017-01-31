import java.io.*;  
    import java.net.*; 
    public class MyClient 
    {
        public static void main(String[] args) 
        {  

            try
            {      
                Socket soc=new Socket("localhost",2004);  
                DataOutputStream dout=new DataOutputStream(soc.getOutputStream());  
                BufferedReader in = new BufferedReader(new InputStreamReader(soc.getInputStream()));
                PrintWriter out = new PrintWriter(soc.getOutputStream(),true);

                out.println("Hello");
                System.out.println(in.readLine());
                soc.close();
            }catch(Exception e)
            {
                e.printStackTrace();
            }
        }
    } 