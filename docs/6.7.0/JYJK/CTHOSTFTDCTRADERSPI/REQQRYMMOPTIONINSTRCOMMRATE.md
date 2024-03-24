<p>请求查询做市商期权合约手续费</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYMMOPTIONINSTRCOMMRATE/">OnRspQryMMOptionInstrCommRate</a></p>
<span class="anchor" id="791073a8-8440-4a01-954d-dec4dcce3732"></span>
## 1.函数原型
<p>virtual int ReqQryMMOptionInstrCommRate(CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="e9dae161-1c21-4467-af73-ecfef15a4949"></span>
## 2.参数
<p>pQryMMOptionInstrCommRate：做市商期权手续费率查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="185f9851-8c34-4179-be4c-d992c7a111a2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="bef47e99-7f35-4008-a733-327f0a6b985c"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="83a3e592-9dc0-43f4-a4f1-d1d27ce5a6a9"></span>
## 5.FAQ
<p>无</p>
