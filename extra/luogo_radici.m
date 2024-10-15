% Creazione della funzione di trasferimento
s = tf("s");

N = s+3;
D = (s+1)*(s+5)*(s+10);
sys = N/D;

% Generazione del grafico del luogo delle radici
figure;
rlocus(sys);
title('Luogo delle radici del sistema K(s+3) + (s+1)(s+5)(s+10)');
grid on;
saveas(gcf, 'luogo_delle_radici.png');