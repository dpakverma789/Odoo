odoo.define('school2.template_preview', function(require){

    var BasicFields = require('web.basic_fields');
    var DocumentViewer = require('mail.DocumentViewer');
    var core = require('web.core');
    var QWeb = core.qweb;

    BasicFields.FieldBinaryFile.include({

        events: _.extend({}, BasicFields.FieldBinaryFile.prototype.events, {
            'click .new_preview_pdf': "new_onAttachmentView",
        }),

        _renderReadonly: function(){
            var self = this;
            self._super.apply(this,arguments);
            if (!self.res_id) {
                self.$el.css('cursor', 'not-allowed');
            } else {
                self.$el.css('cursor', 'pointer');
                self.$el.attr('title', 'Download');
            }
            self.$el.append(QWeb.render("test_q"));
        },

        new_onAttachmentView: function (ev) {
             debugger;
             ev.preventDefault()
             ev.stopPropagation()

             var attachment = [{
                                    filename: this.filename_value,
                                    id:this.recordData.id,
                                    is_main: false,
                                    mimetype: this.recordData.mimetype,
                                    name: this.filename_value,
                                    type: this.recordData.mimetype,
                                    url: "/web/content/" + this.recordData.id + "?download=true",
                                }]
             var activeAttachmentID = this.recordData.id;
             var attachmentViewer = new DocumentViewer(this, attachment, activeAttachmentID);
             attachmentViewer.appendTo($('body'));
        },

    });

});
