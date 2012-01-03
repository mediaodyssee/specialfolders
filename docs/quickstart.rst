.. _quickstart:

Quickstart
==========

Getting the path of a specific folder
-------------------------------------

Desktop folder::
    
    import specialfolders
    print(specialfolders.get_desktop_folder())

Documents folder::
    
    import specialfolders
    print(specialfolders.get_desktop_folder())

Pictures folder::
    
    import specialfolders
    print(specialfolders.get_desktop_folder())

Videos folder::
    
    import specialfolders
    print(specialfolders.get_desktop_folder())

Downloads folder::
    
    import specialfolders
    print(specialfolders.get_desktop_folder())


Retrieving all special folders at once in a dictionary
------------------------------------------------------

If you want to retrieve all special folders pathes at once, just do::

    import specialfolders
    d = specialfolders.get_all_special_folders()

The result is a dictionary that looks like this::

    {
        'documents': u'/home/izi/Documents',
        'videos': u'/home/izi/Vid\xe9os',
        'pictures': u'/home/izi/Images',
        'downloads': u'/home/izi/T\xe9l\xe9chargements',
        'desktop': u'/home/izi/Bureau',
        'music': u'/home/izi/Musique'
    }
