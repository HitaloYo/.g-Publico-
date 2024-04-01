import java.util.Scanner;

public class Conta {
    private String numeroConta;
    private double saldo;
    private double taxaRendimento;

    // Construtor
    public Conta(String numeroConta, double saldo, double taxaRendimento) {
        this.numeroConta = numeroConta;
        this.saldo = saldo;
        this.taxaRendimento = taxaRendimento;
    }

    // Métodos getters
    public String getNumeroConta() {
        return numeroConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public double getTaxaRendimento() {
        return taxaRendimento;
    }

    // Método para sacar dinheiro da conta
    public void saca(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque de R$" + valor + " realizado com sucesso.");
        } else {
            System.out.println("Saldo insuficiente para realizar o saque.");
        }
    }

    // Método para depositar dinheiro na conta
    public void deposita(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito de R$" + valor + " realizado com sucesso.");
        } else {
            System.out.println("Valor de depósito inválido.");
        }
    }

    // Método para calcular o rendimento da conta
    public double calculaRendimento() {
        return saldo * (taxaRendimento / 100);
    }

    // Método para obter os dados da conta
    public void getDadosConta() {
        System.out.println("Número da Conta: " + numeroConta);
        System.out.println("Saldo: R$" + saldo);
        System.out.println("Taxa de Rendimento: " + taxaRendimento + "%");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o número da conta: ");
        String numeroConta = scanner.nextLine();

        System.out.print("Digite o saldo inicial da conta: ");
        double saldoInicial = scanner.nextDouble();

        System.out.print("Digite a taxa de rendimento da conta (%): ");
        double taxaRendimento = scanner.nextDouble();

        Conta minhaConta = new Conta(numeroConta, saldoInicial, taxaRendimento);

        // Menu de interação com o usuário
        int opcao;
        do {
            System.out.println("\n### Menu ###");
            System.out.println("1. Sacar");
            System.out.println("2. Depositar");
            System.out.println("3. Calcular Rendimento");
            System.out.println("4. Mostrar Dados da Conta");
            System.out.println("0. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Digite o valor a sacar: ");
                    double valorSaque = scanner.nextDouble();
                    minhaConta.saca(valorSaque);
                    break;
                case 2:
                    System.out.print("Digite o valor a depositar: ");
                    double valorDeposito = scanner.nextDouble();
                    minhaConta.deposita(valorDeposito);
                    break;
                case 3:
                    double rendimento = minhaConta.calculaRendimento();
                    System.out.println("Rendimento: R$" + rendimento);
                    break;
                case 4:
                    minhaConta.getDadosConta();
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        } while (opcao != 0);

        scanner.close();
    }
}
