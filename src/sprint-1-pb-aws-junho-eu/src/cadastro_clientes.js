// Factory para criar objetos Cliente
function ClienteFactory() {
    function criarCliente(nome, dataNascimento, telefone, email) {
        return {
            nome,
            dataNascimento,
            telefone,
            email
        };
    }

    return {
        criarCliente
    };
}

// Funções para manipular localStorage
const storageKey = 'clientes';

function salvarClientes(clientes) {
    localStorage.setItem(storageKey, JSON.stringify(clientes));
}

function recuperarClientes() {
    const clientes = localStorage.getItem(storageKey);
    const clientesArray = clientes ? JSON.parse(clientes) : [];
    console.log('Clientes recuperados do localStorage:', clientesArray);
    return clientesArray;
}

function adicionarClienteAoLocalStorage(cliente) {
    const clientes = recuperarClientes();
    clientes.push(cliente);
    salvarClientes(clientes);
    console.log('Cliente adicionado ao localStorage:', cliente);
    console.log('Clientes no localStorage após adição:', clientes);
}

function excluirClienteDoLocalStorage(index) {
    const clientes = recuperarClientes();
    const clienteExcluido = clientes[index];
    clientes.splice(index, 1); // Remove o cliente do índice especificado
    salvarClientes(clientes);
    console.log('Cliente excluído do localStorage:', clienteExcluido);
    console.log('Clientes no localStorage após exclusão:', clientes);
}

// Função para exibir os clientes na página
function exibirClientes() {
    const listaCadastro = document.getElementById('listaCadastro');
    listaCadastro.innerHTML = '';

    const clientes = recuperarClientes();
    console.log('Clientes recuperados para exibição na página:', clientes);

    clientes.forEach((cliente, index) => {
        const clienteElement = document.createElement('div');
        clienteElement.classList.add('cliente-item');
        clienteElement.innerHTML = `
            <p><strong>Nome:</strong> ${cliente.nome}</p>
            <p><strong>Data de Nascimento:</strong> ${cliente.dataNascimento}</p>
            <p><strong>Telefone:</strong> ${cliente.telefone}</p>
            <p><strong>Email:</strong> ${cliente.email}</p>
            <button class="btn-excluir">Excluir</button>
            <hr>
        `;
        listaCadastro.appendChild(clienteElement);

// Adicionar evento de clique para o botão Excluir
        const btnExcluir = clienteElement.querySelector('.btn-excluir');
        btnExcluir.addEventListener('click', () => {
            excluirClienteDoLocalStorage(index);
            exibirClientes(); // Atualiza a exibição dos clientes na página após exclusão
        });
    });
}

// Evento de submit do formulário para cadastrar cliente
const formCadastro = document.getElementById('formCadastro');
formCadastro.addEventListener('submit', function(event) {
    event.preventDefault();

    const nome = formCadastro.nome.value;
    const dataNascimento = formCadastro.dataNascimento.value;
    const telefone = formCadastro.tel.value;
    const email = formCadastro.email.value;

    console.log('Dados do formulário de cadastro:', { nome, dataNascimento, telefone, email });

    const factory = ClienteFactory();
    const novoCliente = factory.criarCliente(nome, dataNascimento, telefone, email);

    adicionarClienteAoLocalStorage(novoCliente);
    formCadastro.reset(); // Limpa o formulário após cadastro

    exibirClientes(); // Atualiza a exibição dos clientes na página
});

// Exibir clientes ao carregar a página
window.addEventListener('DOMContentLoaded', () => {
    exibirClientes();
});
