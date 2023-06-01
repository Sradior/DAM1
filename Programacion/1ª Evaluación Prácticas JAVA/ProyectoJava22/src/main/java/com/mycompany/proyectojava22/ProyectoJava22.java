
package com.mycompany.proyectojava22;

import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.RenderingHints;
import javax.swing.JFrame;
import javax.swing.JPanel;


public class ProyectoJava22 extends JPanel{
    
    Persona bolita = new Persona();
    float x = 200; //defnino una posicion inicial
    float y = 200;
    float direccion = 2; //direccion inicial 
    @Override //yo programo mi propio paint
    public void paint(Graphics g){ //sobreescribo el metodo de pintura por defecto 
        super.paint(g); //pinto en la ventana principal 
        Graphics2D graf2d = (Graphics2D) g; //creo un nuevo elemento de graficos 2d
        graf2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON); //suaviza los pixeles de la bola
        graf2d.fillOval((int)x,(int)y,20,20); //dibujo ovalo 
    }
    public void moverBola(){ //esta funcion mueve la bola 
        double min = -0.5; // establezco un minimo 
        double max = 0.5; // maximo 
        double random = min + Math.random() * (max - min); //creo un NO aleatorio entre min y max
        direccion += random; //vario la direccion de forma aleatoria 
        x += Math.cos(direccion); // aumento la x en base a la direccion y su coseno
        y += Math.sin(direccion); // aumento la y en base a la direccion y su seno
        if(x > 400){direccion += Math.PI;} // en caso de que x sea menor de 400, da la vuelta
        if(x < 0){direccion += Math.PI;} // pega la vuelta al colisionar
        if(y > 400){direccion += Math.PI;} // pega la vuelta al colisionar
        if(y < 0){direccion += Math.PI;} // pega la vuelta al colisionar
    }
    public static void main(String[] args) throws InterruptedException{ //funcion principal 
        JFrame marco = new JFrame ("animacion"); //creo un marco de swing 
        ProyectoJava22 jueguito = new ProyectoJava22(); // creo una instancia del proyecto
        marco.add(jueguito); //al marco, le añado el proyecto
        marco.setSize(400,400); //especifico las dimensiones de la ventana 
        marco.setVisible(true); // le digo que la ventana sea visible
        marco.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //cierra el programa al cerrar la ventana
        
        while(true){ //bucle infinito 
            jueguito.moverBola(); //mueve la bola 
            jueguito.repaint();// repitan lo que hay en la pantalla
            System.out.println("Hola"); //
            Thread.sleep(10); // se ejecuta múltiples veces en bucle
        }
    }
}
