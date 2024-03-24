<p>合约状态变化表示的是交易所各合约的交易阶段变化，用户在登录CTP后，无需订阅便能收到全量的合约状态变化（对应接口<a href="../../JYJK/CTHOSTFTDCTRADERAPI/ONRTNINSTRUMENTSTATUS/">OnRtnInstrumentStatus</a>），该变化在盘中实时推送。其中合约状态推送到产品级别，期权也是推送到产品级别的。CTP服务器预埋单便是通过判断合约是否进入集合竞价报单阶段或连续交易阶段来触发的。本文整理了各交易所的合约状态变化。</p>
<span class="anchor" id="483b05e0-eb56-4dfb-a11e-80a8b3f05150"></span>
## 1.各交易所合约状态变化
<p>下图是交易所各个时间段的报盘状态变化情况。</p>
<table><tr><th style="TEXT-ALIGN: center;">　</th><th style="TEXT-ALIGN: center;">CFFEX</th><th style="TEXT-ALIGN: center;">CZCE</th><th style="TEXT-ALIGN: center;">DCE</th><th style="TEXT-ALIGN: center;">INE</th><th style="TEXT-ALIGN: center;">SHFE</th></tr><tr><td style="TEXT-ALIGN: center;">20:55:00</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">20:59:00</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">开盘前</td>
<td style="TEXT-ALIGN: center;">集合竞价撮合</td>
<td style="TEXT-ALIGN: center;">集合竞价撮合</td>
<td style="TEXT-ALIGN: center;">集合竞价撮合</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">21:00:00</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">8:55:00</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">8:59:00</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">开盘前</td>
<td style="TEXT-ALIGN: center;">非交易</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">非交易</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">9:00:00</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">9:10:00</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">9:14:00</td>
<td style="TEXT-ALIGN: center;">集合竞价撮合</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">9:15:00</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">9:25:00</td>
<td style="TEXT-ALIGN: center;">集合竞价报单</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">9:29:00</td>
<td style="TEXT-ALIGN: center;">集合竞价撮合</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">9:30:00</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">10:15:00</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">开盘前</td>
<td style="TEXT-ALIGN: center;">非交易</td>
<td style="TEXT-ALIGN: center;">非交易</td>
<td style="TEXT-ALIGN: center;">非交易</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">10:30:00</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">11:30:00</td>
<td style="TEXT-ALIGN: center;">非交易</td>
<td style="TEXT-ALIGN: center;">开盘前</td>
<td style="TEXT-ALIGN: center;">非交易</td>
<td style="TEXT-ALIGN: center;">非交易</td>
<td style="TEXT-ALIGN: center;">非交易</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">13:00:00</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
<td style="TEXT-ALIGN: center;">连续交易</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">15:00:00</td>
<td style="TEXT-ALIGN: center;">收盘</td>
<td style="TEXT-ALIGN: center;">收盘</td>
<td style="TEXT-ALIGN: center;">收盘</td>
<td style="TEXT-ALIGN: center;">收盘</td>
<td style="TEXT-ALIGN: center;">收盘</td>
</tr>
<tr><td style="TEXT-ALIGN: center;">15:15:00</td>
<td style="TEXT-ALIGN: center;">收盘</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
<td style="TEXT-ALIGN: center;">　</td>
</tr>
</table>
<span class="anchor" id="71a65d20-cf1e-4f09-b715-89e9aa20dfa6"></span>
## 2.关于EnterTime字段
<p>EnterTime表示的是进入本状态时间，该时间指的是交易所时间；但郑商所例外，因为郑商所的合约状态变化是通过交易所的行情报盘推送的，其中没有时间戳，因此CTP会打上排队机时间戳，也就是说郑商所的合约状态变化报文中的EnterTime表示的是CTP排队机的时间。</p>
