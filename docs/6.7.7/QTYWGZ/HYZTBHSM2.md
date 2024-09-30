<p>合约状态变化表示的是交易所各合约的交易阶段变化，用户在登录CTP后，无需订阅便能收到全量的合约状态变化（对应接口<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNINSTRUMENTSTATUS/">OnRtnInstrumentStatus</a>），该变化在盘中实时推送。其中合约状态推送到产品级别，期权也是推送到产品级别的。CTP服务器预埋单便是通过判断合约是否进入集合竞价报单阶段或连续交易阶段来触发的。本文整理了各交易所的合约状态变化。</p>
<span class="anchor" id="1d23bd1d-2251-420b-83b5-9131be9a82dc"></span>
## 1.各交易所合约状态变化
<p>合约交易状态：</p>
<p>开盘前：0</p>
<p>非交易：1</p>
<p>连续交易：2</p>
<p>集合竞价报单：3</p>
<p>集合竞价价格平衡：4</p>
<p>集合竞价撮合：5</p>
<p>收盘：6</p>
<span class="anchor" id="9dcd6518-a293-423a-97c4-b3f9018db275"></span>
### 1.1.SHFE合约状态
<p>推送方式：交易所推送合约级别，ctp推送产品级别</p>
<div style="width: 80%;overflow-x: auto;white-space: nowrap;text-align:center">
<table border="1" cellpadding="0">
<tr bgcolor="#0062A8" height="38" style="white-space: nowrap">
<th height="38" width="56">
<font color="#FFFFFF" face="微软雅黑">合约</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">开盘前</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">20:55</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">20:59</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">21:00</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">23:00</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">1:00</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">2:30</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">开盘前</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">8:55</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">8:59</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">9:00</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">10:15</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">10:30</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">11:30</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">13:30</font>
</th>
<th>
<font color="#FFFFFF" face="微软雅黑">15:00</font>
</th>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ag</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td></td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">al</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ao</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">cu</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ni</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">pb</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">zn</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">sn</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ss</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">au</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">fu</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">hc</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">bu</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">rb</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ru</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">sp</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">wr</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
</table>
</div>
<span class="anchor" id="06579334-b629-434d-bb77-4cf5a7c15bf6"></span>
### 1.2.INE合约状态
<p>推送方式：交易所推送合约级别，ctp推送产品级别</p>
<div style="width: 80%;overflow-x: auto;white-space: nowrap">
<table border="1" cellpadding="0">
<tr bgcolor="#0062A8" height="38" style="white-space: nowrap">
<th height="38" width="56">
<font color="#FFFFFF" face="微软雅黑">合约</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">开盘前</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">20:55</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">20:59</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">21:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">23:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">1:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">2:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">8:55</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">8:59</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">9:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">10:15</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">10:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">11:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">13:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">15:00</font>
</th>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">bc</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td>1</td>
<td></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">lu</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">nr</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td></td>
<td></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">sc</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td></td>
<td></td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
</table>
</div>
<span class="anchor" id="4c31b86a-4efa-4b96-bfbc-0562a2172fd0"></span>
### 1.3.CZCE合约状态
<p><span alt="" id="anchor-id-01"></span> </p>
<p>推送方式：交易所推送产品级别，ctp推送产品级别（郑商所合约状态基于5期环境整理）</p>
<div style="width: 80%;overflow-x: auto;white-space: nowrap">
<table border="1" cellpadding="0">
<tr bgcolor="#0062A8" height="38" style="white-space: nowrap">
<th height="38" width="56">
<font color="#FFFFFF" face="微软雅黑">产品</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">20:55</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">20:59</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">21:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">23:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">8:55</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">8:59</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">9:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">10:15</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">10:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">11:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">13:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">15:00</font>
</th>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">CF</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">CY</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">FG</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">MA</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ME</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">OI</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">PF</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">RM</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">SA</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">SR</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">TA</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">TC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ZC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">CFC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">CFP</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">MAC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">MAP</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">OIC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">OIP</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">RMC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">RMP</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">SRC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">SRP</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">TAC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">TAP</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ZCC</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ZCP</td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td></td>
<td></td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">AP</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">CJ</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">ER</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">JR</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">LR</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">PK</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">PM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">RI</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">RO</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">RS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">SF</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">SM</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">UR</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">WH</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">WS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">WT</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">PKC</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">PKP</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>0</td>
<td>2</td>
<td>6</td>
</tr>
</table>
</div>
<span class="anchor" id="83335217-cb3e-43bd-9415-8d15637c79ba"></span>
### 1.4.DCE合约状态
<p>推送方式：交易所推送产品级别，ctp推送产品级别</p>
<div style="width: 80%;overflow-x: auto;white-space: nowrap">
<table border="1" cellpadding="0">
<tr bgcolor="#0062A8" height="38" style="white-space: nowrap">
<th height="38" width="56">
<font color="#FFFFFF" face="微软雅黑">产品</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">20:55</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">20:59</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">21:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">23:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">8:55</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">8:59</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">9:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">10:15</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">10:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">11:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">13:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">15:00</font>
</th>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">a</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">a_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">b</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">b_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">c</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">c_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">cs</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">eb</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">eb_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">eg</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">eg_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">i</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">i_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">j</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">jm</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">l</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">l_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">m</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">m_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">p</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">p_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">pg</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">pg_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">pp</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">pp_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">rr</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">v</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">v_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">y</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">y_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">bb</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">fb</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">jd</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">lh</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
</table>
</div>
<span class="anchor" id="d60fe113-05ea-4862-b345-9249feb8151e"></span>
### 1.5.CFFEX合约状态
<p>推送方式：交易所推送合约级别，ctp推送产品级别</p>
<div style="width: 80%;overflow-x: auto;white-space: nowrap">
<table border="1" cellpadding="0">
<tr bgcolor="#0062A8" height="38" style="white-space: nowrap">
<th height="38" width="56">
<font color="#FFFFFF" face="微软雅黑">产品</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">开盘前</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">9:25</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">9:29</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">9:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">11:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">13:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">14:57</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">15:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">15:15</font>
</th>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">IC</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td></td>
<td>6</td>
<td></td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">IF</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td></td>
<td>6</td>
<td></td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">IH</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td></td>
<td>6</td>
<td></td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">IM</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td></td>
<td>6</td>
<td></td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">TL</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td></td>
<td>6</td>
<td></td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">T</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td></td>
<td></td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">TF</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td></td>
<td></td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">TS</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td></td>
<td></td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">IO期权</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>5/6</td>
<td></td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">MO期权</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>5/6</td>
<td></td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">HO期权</td>
<td>0</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>5/6</td>
<td></td>
</tr>
</table>
</div>
<span class="anchor" id="4086261d-12a2-49e1-a2ec-74278c7d3766"></span>
### 1.6.GFEX合约状态
<p>推送方式：交易所推送产品级别，ctp推送产品级别</p>
<div style="width: 80%;overflow-x: auto;white-space: nowrap">
<table border="1" cellpadding="0">
<tr bgcolor="#0062A8" height="38" style="white-space: nowrap">
<th height="38" width="56">
<font color="#FFFFFF" face="微软雅黑">产品</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">8:55</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">8:59</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">9:00</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">10:15</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">10:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">11:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">13:30</font>
</th>
<th align="right">
<font color="#FFFFFF" face="微软雅黑">15:00</font>
</th>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">si</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
<tr height="19" style="height:14.25pt">
<td height="19" style="height:14.25pt">si_o</td>
<td>3</td>
<td>5</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>6</td>
</tr>
</table>
</div>
<span class="anchor" id="d0861862-3246-4575-a0ea-f8d023d9d9ef"></span>
## 2.关于EnterTime字段
<p>EnterTime表示的是进入本状态时间，该时间指的是交易所时间；但郑商所例外，因为郑商所的合约状态变化是通过交易所的行情报盘推送的，其中没有时间戳，因此CTP会打上排队机时间戳，也就是说郑商所的合约状态变化报文中的EnterTime表示的是CTP排队机的时间。</p>
