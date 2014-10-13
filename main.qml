import QtQuick 2.3
import QtQuick.Controls 1.2
import QtQuick.Layouts 1.1
import QtWebKit 3.0

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: qsTr("InfoDash")

    ColumnLayout {
        anchors.fill: parent

        GridLayout {
            rows: 3
            flow: GridLayout.TopToBottom
            anchors.fill: parent

            WebView {
                url: 'http://dikutal.dk'
                Layout.fillHeight: true
                Layout.fillWidth: true
            }

            WebView {
                url: 'http://diku.dk'
                Layout.fillHeight: true
                Layout.fillWidth: true
            }

            WebView {
                url: 'http://diku.dk'
                Layout.fillHeight: true
                Layout.fillWidth: true
            }

            WebView {
                url: 'http://dikultur.dk'
                Layout.rowSpan: 3
                Layout.fillHeight: true
                Layout.fillWidth: true
            }

        }
        Text {
            text: 'Hello world'
            Layout.alignment: Text.AlignRight
        }
    }
}
