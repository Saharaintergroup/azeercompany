odoo.define('azeer_theme.portfolio', function (require) {
'use strict';

const options = require('web_editor.snippets.options');

options.registry.PortLayout = options.registry.SelectTemplate.extend({
    /**
     * @constructor
     */
    init() {
        this._super(...arguments);
        this.containerSelector = '> .container, > .container-fluid, > .o_container_small';
        this.selectTemplateWidgetName = 'port_shades';
    },
});


});
