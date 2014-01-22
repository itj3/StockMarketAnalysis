//main.cpp is the main class for the GUI

#include <gtk/gtk.h>

GtkBuilder *builder;
GtkWidget *window;
GtkWidget *windowNT;
GtkWidget *entryNA;

void enter_callback( GtkWidget *widget, GtkWidget *entry){
  const gchar *entry_text;
  entry_text = gtk_entry_get_text (GTK_ENTRY (entry));
  g_print("Entry contents: %s\n", entry_text);
}

void entryNA_active(GtkWidget *widget, gpointer data){
	gtk_entry_set_text(GTK_ENTRY(entryNA), "hello");
	g_print("hello");
}

void on_window_destroy (GtkObject *object, gpointer user_data){
	gtk_main_quit();
}


int main (int argc, char *argv[]){
    g_print("sup dawg");

    gtk_init (&argc, &argv);
        
    builder = gtk_builder_new();
    gtk_builder_add_from_file(builder, "GUI.glade", NULL);

    window = GTK_WIDGET(gtk_builder_get_object (builder, "windowMain"));
	windowNT = GTK_WIDGET(gtk_builder_get_object (builder, "windowNT"));
	entryNA = GTK_WIDGET(gtk_builder_get_object (builder, "entryNA"));

	g_signal_connect(G_OBJECT(entryNA), "activate", G_CALLBACK(entryNA_active), entryNA);

    gtk_builder_connect_signals(builder, NULL);   
    g_object_unref(G_OBJECT (builder));
   
    gtk_widget_show (window);       
    gtk_main ();
        
    return 0;
}