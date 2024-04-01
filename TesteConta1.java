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
        Conta minhaConta = new Conta("12345", 1000.0, 0.5);
        minhaConta.deposita(500.0);
        minhaConta.saca(200.0);
        double rendimento = minhaConta.calculaRendimento();
        System.out.println("Rendimento: R$" + rendimento);
        minhaConta.getDadosConta();
    }
}