/*
 * Copyright (C) 2014 Glyptodon LLC
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

/**
 * Service which defines the Form class.
 */
angular.module('rest').factory('Form', [function defineForm() {

    /**
     * The object returned by REST API calls when representing the data
     * associated with a form or set of configuration parameters.
     *
     * @constructor
     * @param {Form|Object} [template={}]
     *     The object whose properties should be copied within the new
     *     Form.
     */
    var Form = function Form(template) {

        // Use empty object by default
        template = template || {};

        /**
         * The name which uniquely identifies this form, or null if this form
         * has no name.
         *
         * @type String
         */
        this.name = template.name;

        /**
         * All fields contained within this form.
         *
         * @type Field[]
         */
        this.fields = template.fields || [];

    };

    return Form;

}]);
