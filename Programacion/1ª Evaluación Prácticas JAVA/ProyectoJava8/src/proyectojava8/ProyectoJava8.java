package proyectojava8;

public class ProyectoJava8 {

    public static void main(String[] args) {
        String diasemana="patata";
        
        switch(diasemana){
            case "lunes":
                System.out.println("Hoy es el peor dia de la semana");break;
            case "martes":
                System.out.println("Ya queda menos");break;
            case "miercoles":
                System.out.println("Poco a poco ya es viernes");break;
            case "jueves":
                System.out.println("Jueves que huele a viernes");break;
            case "viernes":
                System.out.println("Porfin viernes");break;
            case "sabado":
                System.out.println("Hoy es el mejor dia de la semana sabado de chill");break;
            case "domingo":
                System.out.println("Vuelta a la mala vida");break;
            default:
                System.out.println("Eso no es un dia");break;
            
        }//switch para evaluar más de un caso (case) break para pasar al siguiente caso
    }
    
}
