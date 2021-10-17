//1. Making A Network Request To Fetch Some JSON and print the result
import axios from 'axios';

const url="https://jsonplaceholder.typicode.com/todos"



const sendGetRequest = async () => {
    try {
        const resp = await axios.get('https://jsonplaceholder.typicode.com/todos');
        console.log(resp.data);
    } catch (err) {
        // Handle Error Here
        console.error(err);
    }
};

sendGetRequest();
