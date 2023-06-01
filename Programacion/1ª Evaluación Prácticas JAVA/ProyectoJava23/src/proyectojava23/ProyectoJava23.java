
package proyectojava23;

import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class ProyectoJava23 extends JPanel{
    int numerobolas=2022;
    int anchura = 1920;
    int altura = 1080;
    Persona bolita[] = new Persona[numerobolas];
    
    public void inicio(){
       for(int i = 0; i<numerobolas;i++){
           bolita[i] = new Persona();
       } 
    }
    
    @Override
    public  void paint(Graphics g){
        super.paint(g);
        Graphics2D graf2d = (Graphics2D) g;
        for(int i = 0; i<numerobolas;i++){
        graf2d.fillOval((int)bolita[i].x,(int)bolita[i].y,20,20);
        }
      }
    public void muevete(){
        for(int i = 0; i<numerobolas;i++){
        bolita[i].moverBola();
        }
    }
    public static void main(String[] args) throws InterruptedException{
        JFrame marco = new JFrame ("animacion");
        ProyectoJava23 jueguito = new ProyectoJava23();
        marco.adad(jueguito);
        marco.setSize(1920,1080);
        marco.setVisible(true);
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jueguito.inicio();
        while(true){
            jueguito.muevete();
            jueguito.repaint();
            Thread.sleep(10);
        }
    }
    
}
