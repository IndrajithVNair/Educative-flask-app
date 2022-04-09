from flask import Flask, render_template

app = Flask(__name__)

@app.route('/auth-forgot-password-basic.html')
def auth_forgot_password_basic():
    return render_template('auth-forgot-password-basic.html')

@app.route('/auth-login-basic.html')
def auth_login_basic():
    return render_template('auth-login-basic.html')

@app.route('/auth-register-basic.html')
def auth_register_basic():
    return render_template('auth-register-basic.html')

@app.route('/cards-basic.html')
def cards_basic():
    return render_template('cards-basic.html')

@app.route('/extended-ui-perfect-scrollbar.html')
def extended_ui_perfect_scrollbar():
    return render_template('extended-ui-perfect-scrollbar.html')

@app.route('/extended-ui-text-divider.html')
def extended_ui_text_divider():
    return render_template('extended-ui-text-divider.html')

@app.route('/form-layouts-horizontal.html')
def form_layouts_horizonta():
    return render_template('form-layouts-horizontal.html')

@app.route('/form-layouts-vertical.html')
def form_layouts_vertica():
    return render_template('form-layouts-vertical.html')

@app.route('/forms-basic-inputs.html')
def forms_basic_inputs():
    return render_template('forms-basic-inputs.html')

@app.route('/forms-input-groups.html')
def forms_input_groups():
    return render_template('forms-input-groups.html')

@app.route('/icons-boxicons.html')
def icons_boxicons():
    return render_template('icons-boxicons.html')

@app.route('/index.html')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layouts-blank.html')
def ayouts_blank():
    return render_template('layouts-blank.html')

@app.route('/layouts-container.html')
def ayouts_container():
    return render_template('layouts-container.html')

@app.route('/layouts-fluid.html')
def ayouts_fluid():
    return render_template('layouts-fluid.html')

@app.route('/layouts-without-menu.html')
def ayouts_without_menu():
    return render_template('layouts-without-menu.html')

@app.route('/layouts-without-navbar.html')
def ayouts_without_navbar():
    return render_template('layouts-without-navbar.html')

@app.route('/pages-account-settings-account.html')
def pages_account_settings_accoun():
    return render_template('pages-account-settings-account.html')

@app.route('/pages-account-settings-connections.html')
def pages_account_settings_connections():
    return render_template('pages-account-settings-connections.html')

@app.route('/pages-account-settings-notifications.html')
def pages_account_settings_notifications():
    return render_template('pages-account-settings-notifications.html')

@app.route('/pages-misc-error.html')
def pages_misc_error():
    return render_template('pages-misc-error.html')

@app.route('/pages-misc-under-maintenance.html')
def pages_misc_under_maintenance():
    return render_template('pages-misc-under-maintenance.html')

@app.route('/tables-basic.html')
def ables_basic():
    return render_template('tables-basic.html')

@app.route('/ui-accordion.html')
def ui_accordion():
    return render_template('ui-accordion.html')

@app.route('/ui-alerts.html')
def ui_alerts():
    return render_template('ui-alerts.html')

@app.route('/ui-badges.html')
def ui_badges():
    return render_template('ui-badges.html')

@app.route('/ui-buttons.html')
def ui_buttons():
    return render_template('ui-buttons.html')

@app.route('/ui-carousel.html')
def ui_carouse():
    return render_template('ui-carousel.html')

@app.route('/ui-collapse.html')
def ui_collapse():
    return render_template('ui-collapse.html')

@app.route('/ui-dropdowns.html')
def ui_dropdowns():
    return render_template('ui-dropdowns.html')

@app.route('/ui-footer.html')
def ui_footer():
    return render_template('ui-footer.html')

@app.route('/ui-list-groups.html')
def ui_list_groups():
    return render_template('ui-list-groups.html')

@app.route('/ui-modals.html')
def ui_modals():
    return render_template('ui-modals.html')

@app.route('/ui-navbar.html')
def ui_navbar():
    return render_template('ui-navbar.html')

@app.route('/ui-offcanvas.html')
def ui_offcanvas():
    return render_template('ui-offcanvas.html')

@app.route('/ui-pagination-breadcrumbs.html')
def ui_pagination_breadcrumbs():
    return render_template('ui-pagination-breadcrumbs.html')

@app.route('/ui-progress.html')
def ui_progress():
    return render_template('ui-progress.html')

@app.route('/ui-spinners.html')
def ui_spinners():
    return render_template('ui-spinners.html')

@app.route('/ui-tabs-pills.html')
def ui_tabs_pills():
    return render_template('ui-tabs-pills.html')

@app.route('/ui-toasts.html')
def ui_toasts():
    return render_template('ui-toasts.html')

@app.route('/ui-tooltips-popovers.html')
def ui_tooltips_popovers():
    return render_template('ui-tooltips-popovers.html')

@app.route('/ui-typography.html')
def ui_typography():
    return render_template('ui-typography.html')

if __name__ == '__main__':
    app.run()