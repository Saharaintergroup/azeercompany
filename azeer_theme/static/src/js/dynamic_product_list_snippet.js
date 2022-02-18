odoo.define('azeer_theme.s_dynamic_snippet_products', function (require) {
'use strict';
const config = require('web.config');
const core = require('web.core');
const publicWidget = require('web.public.widget');
const DynamicSnippetCarousel = require('website.s_dynamic_snippet_carousel');
var wSaleUtils = require('website_sale.utils');

const DynamicAzeerSnippetProducts = DynamicSnippetCarousel.extend({
    selector: '.s_dynamic_snippet_products',
    read_events: {
        'click a.js_add_cart_json': '_onClickAddCartJSON',
       'click div.js_select_image': '_onClickImage',
       'click .js_azeer_add_cart': '_onClickAddCart',      
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * Method to be overridden in child components in order to provide a search
     * domain if needed.
     * @override
     * @private
     */
    _getSearchDomain: function () {
        const searchDomain = this._super.apply(this, arguments);
        let productCategoryId = this.$el.get(0).dataset.productCategoryId;
        if (productCategoryId && productCategoryId !== 'all') {
            if (productCategoryId === 'current') {
                productCategoryId = undefined;
                const productCategoryField = $("#product_details").find(".product_category_id");
                if (productCategoryField && productCategoryField.length) {
                    productCategoryId = parseInt(productCategoryField[0].value);
                }
                if (!productCategoryId) {
                    this.trigger_up('main_object_request', {
                        callback: function (value) {
                            if (value.model === "product.public.category") {
                                productCategoryId = value.id;
                            }
                        },
                    });
                }
                if (!productCategoryId) {
                    // Try with categories from product, unfortunately the category hierarchy is not matched with this approach
                    const productTemplateId = $("#product_details").find(".product_template_id");
                    if (productTemplateId && productTemplateId.length) {
                        searchDomain.push(['public_categ_ids.product_tmpl_ids', '=', parseInt(productTemplateId[0].value)]);
                    }
                }
            }
            if (productCategoryId) {
                searchDomain.push(['public_categ_ids', 'child_of', parseInt(productCategoryId)]);
            }
        }
        const productNames = this.$el.get(0).dataset.productNames;
        if (productNames) {
            const nameDomain = [];
            for (const productName of productNames.split(',')) {
                if (nameDomain.length) {
                    nameDomain.unshift('|');
                }
                nameDomain.push(['name', 'ilike', productName]);
            }
            searchDomain.push(...nameDomain);
        }
        return searchDomain;
    },

    /**
     * @override
     */
    _getRpcParameters: function () {
        const productTemplateId = $("#product_details").find(".product_template_id");
        return Object.assign(this._super.apply(this, arguments), {
            productTemplateId: productTemplateId && productTemplateId.length ? productTemplateId[0].value : undefined,
        });
    },

    /**
     * @private
     * @param {MouseEvent} ev
     */
    _onClickAddCart: function (ev){
        var $link = $(ev.currentTarget);
        var self = this;
        var $card = $link.closest('.card');
        var $quntity =parseFloat($link.closest('.input-group').find("input").val() || 1);
        this._rpc({
            route: "/shop/cart/update_json",
            params: {
                product_id: $card.find('input[data-product-id]').data('product-id'),
                add_qty: $quntity
            },
        }).then(function (data) {
            var $navButton = $('header .o_wsale_my_cart').first();
            var fetch = self._fetchData();
            var animation = wSaleUtils.animateClone($navButton, $(ev.currentTarget).parents('.card'), 25, 40);
            Promise.all([fetch, animation]).then(function (values) {
                wSaleUtils.updateCartNavBar(data);
                self._render();
            });
        });
    },


    /**
     * @private
     * @param {MouseEvent} ev
     */
    _onClickAddCartJSON: function (ev){
        ev.preventDefault();
        var $link = $(ev.currentTarget);
        var $input = $link.closest('.input-group').find("input");
        var min = parseFloat($input.data("min") || 0);
        var max = parseFloat($input.data("max") || Infinity);
        var previousQty = parseFloat($input.val() || 0, 10);
        var quantity = ($link.has(".fa-minus").length ? -1 : 1) + previousQty;
        var newQty = quantity > min ? (quantity < max ? quantity : max) : min;

        if (newQty !== previousQty) {
            $input.val(newQty).trigger('change');
        }
        return false;
    },

    /**
     * @private
     * @param {MouseEvent} ev
     */
    _onClickImage :function (ev){
        
        ev.preventDefault();
        var $link = $(ev.currentTarget);
        //var $img = $link.find("img");
        var $image_obj_id = $link.attr("image-obj-id")
        if ($link.hasClass("primary_img")){
            console.log('primary_img image')
            var $active_img = $('.product_banner').find('.img_active')
            $active_img.removeClass("img_active")
            $active_img.addClass("img_inactive")
            var primary_img = $('.product_banner').find('.primary_img')
            primary_img.removeClass("img_inactive")
            primary_img.addClass("img_active")
            return false
        }
        var $active_img = $('.product_banner').find('.img_active')
         
        $active_img.removeClass("img_active")
        $active_img.addClass("img_inactive")

        var $img_divs = $('.product_banner').find('.product_img_div')

        $img_divs.each(function( index ,value) {
            if ($(value).attr("image-obj-id")== $image_obj_id && !$(value).hasClass( "primary_img" )){
                $(value).removeClass("img_inactive")
                $(value).addClass("img_active")
            }
        });       
    },

});
publicWidget.registry.dynamic_snippet_products = DynamicAzeerSnippetProducts;

return DynamicAzeerSnippetProducts;
});
