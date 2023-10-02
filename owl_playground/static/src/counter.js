import {Component} from "@odoo/owl";

class Counter extends Component {
    static template = "my_module.Counter";

    setup() {
        this.state = useState({value: 0});
    }

    increment() {
        this.state.value++;
    }
}