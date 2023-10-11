/** @odoo-module **/

import {Component, useState} from "@odoo/owl";

export class Todo extends Component {
    static template = "owl_playground.todo";

    //iki rung iso
    static props = {
        'id': {type: Number},
        'description': {type: String},
        'done': {type: Boolean}
    };

    setup() {
        this.ngopo = {id: 3, description: "buy milk", done: false};
    }

}
