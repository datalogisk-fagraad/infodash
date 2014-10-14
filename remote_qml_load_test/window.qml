

import QtQuick 2.0
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
import QtWebKit 3.0

ApplicationWindow { 

visible: true
width: 400
height: 400
title: qsTr("foo")

    Loader {
	id: "loader"
	objectName: "Loader"
	source: "blank.qml"
    }

}

