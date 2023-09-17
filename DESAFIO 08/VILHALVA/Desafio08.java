import java.util.Scanner;

public class Desafio08 {
    private static final int calcularMDC(final int a, final int b) {

        if (b == 0) {
            return a;
        }

        return calcularMDC(b, a % b);
    }

    private static class Fracao {

        private final int numerador;
        private final int denominador;

        public Fracao(final int numerador, final int denominador) {
            this.numerador = numerador;
            this.denominador = denominador;
        }

        public Fracao simplificar() {
            final int mdc = calcularMDC(numerador, denominador);
            return new Fracao(numerador / mdc, denominador / mdc);
        }

        @Override
        public String toString() {

            if (denominador == 0) {
                return "ERR";
            }

            if (numerador < denominador) {
                return numerador + "/" + denominador;
            }

            final int resto = numerador % denominador;
            final int novoNumerador = numerador / denominador;

            if (resto == 0) {
                return String.valueOf(novoNumerador);
            }

            return novoNumerador + " " + resto + "/" + denominador;

        }

    }

    public static void main(final String[] args) throws Exception {

        try (Scanner scanner = new Scanner(System.in)) {

            while (scanner.hasNextLine()) {

                final String line = scanner.nextLine();
                final String[] splitted = line.split("/");

                final int numerador = Integer.parseInt(splitted[0]);
                final int denominador = (splitted.length == 2) ? Integer.parseInt(splitted[1]) : 1;

                System.out.println(new Fracao(numerador, denominador).simplificar());

            }
        }
    }
}
