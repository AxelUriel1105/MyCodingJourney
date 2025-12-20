
package englishschoolexercise;
import java.util.Scanner;
public class EnglishSchoolExercise {

    public static void main(String[] args) {
        int age;
        Scanner keyboard = new Scanner(System.in);
        System.out.println("***BIENVENIDO A ENGLISH SCHOOL");
        System.out.println("Ingrese la edad del alumno: ");
        age = keyboard.nextInt();
        if (age >= 4 && age <= 6) {
            System.out.println("El horario del grupo es de: Lunes y Miércoles de 16 a 17hrs");
        } else {
            if (age >= 7 && age <= 8) {
                System.out.println("El horario del grupo es de: Martes y jueves de 16:30 a 17:30 hrs");
            } else {
                if (age >= 9 && age <= 10) {
                    System.out.println("El horario del grupo es de: Martes y jueves 16:30 a 19:00 hrs");
                } else {
                    if (age >= 11 && age <= 13) {
                        System.out.println("El horario es de: Lunes y Miércoles de 17 a 18:30 hrs");
                    } else {
                        System.out.println("Ingreso una edad que no corresponde ");
                    }
                }
            }
        }
    }

}
