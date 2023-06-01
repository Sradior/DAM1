
package graficabbdd;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.DriverManager;

public class GraficaBBDD extends JPanel{
    
    @Override public void paint(Graphics g){
        super.paint(g);
        Graphics2D misgraficos = (Graphics2D)g;
        
        int basegrafica = 360;
        //misgraficos.fillOval(200, 200, 100, 100);
        misgraficos.drawLine(10, 10, 10, 360);
        misgraficos.drawLine(10, basegrafica, 360, basegrafica);
        int [] barras = new int[]{100,200,300,75,300,50};
        
        String url = "jdbc:sqlite:C:/Users/Frank Crespo/Desktop/registros.db";
        Connection conn = null;
        try {
            String sql = "SELECT * FROM logmeses";
            conn = DriverManager.getConnection(url);
            java.sql.Statement stmt  = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            int contador = 0;
            while (rs.next()) {
                System.out.println(rs.getInt("mes") + "\t" +
                                   rs.getString("numero"));
                barras[contador] = Integer.parseInt(rs.getString("numero"));
                contador++;
            }
            
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
   
        for(int i = 0; i<barras.length;i++){
            //int randomNum = ThreadLocalRandom.current().nextInt(10,300 +1);
            int randomNum = barras[i];
            misgraficos.fillRect(i*30+20, basegrafica-randomNum, 10, randomNum);
        }
    }

    public static void main(String[] args) {
        JFrame marco = new JFrame("grafica");
        GraficaBBDD mimarco = new GraficaBBDD();
        marco.add(mimarco);
        marco.setSize(400, 400);
        marco.setVisible(true);
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
}
