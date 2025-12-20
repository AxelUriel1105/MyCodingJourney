
package operadorternario;
import java.util.Scanner;
public class OperadorTernario {

    public static void main(String[] args) {
        // Programa que dependiendo del promedio de un alumno nos diga si aprobó o no una materia
        // declaración de variables
        double average;
        String finalCondition;
        // Pedir el promedio por teclado
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Ingrese el promedio del alumno: ");
        average = keyboard.nextDouble();
        finalCondition = (average >= 6) ? "Aprobado":"Reprobado";
        System.out.println("La condición final del alumno es: "+finalCondition);
    }
    
}
