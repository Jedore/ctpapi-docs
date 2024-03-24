<p>请求查询产品组</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYPRODUCTGROUP/">OnRspQryProductGroup</a></p>
<span class="anchor" id="948543cc-a31f-4579-ae96-1b55ff0e18a0"></span>
## 1.函数原型
<p>virtual int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) = 0;</p>
<span class="anchor" id="cd952a5e-5ec5-4e1f-a59f-9836e8d7f09c"></span>
## 2.参数
<p>pQryProductGroup：查询产品组</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="61bb6888-5750-4c0b-b4cb-8a9a653d559b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="39461415-a162-4e70-ab68-dbcc7f857e3b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="52c567b9-2e20-4931-9589-3ab66f1a8536"></span>
## 5.FAQ
<p>无</p>
