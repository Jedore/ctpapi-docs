<span class="anchor" id="0cfa4dd2-4856-406b-b2e4-361f4861b10a"></span>
## 1.说明
<p>请求查询报单手续费</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINSTRUMENTORDERCOMMRATE/">OnRspQryInstrumentOrderCommRate</a></p>
<span class="anchor" id="bf867649-239d-43da-abea-344b75c34cdc"></span>
## 2.函数原型
<p>virtual int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID) = 0;</p>
<span class="anchor" id="cf682507-3c29-4d27-95a3-5aa007f3aaaf"></span>
## 3.参数
<p>pQryInstrumentOrderCommRate：报单手续费率查询</p>
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
<span class="anchor" id="61a6b59f-7fab-4911-90d5-5aafe5dd6951"></span>
## 4.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4e60fe85-55ab-4792-aab6-4e098de60d0f"></span>
## 5.调用示例
<pre><code>CThostFtdcQryInstrumentOrderCommRateField a = { 0 };
strcpy(a.BrokerID, "9999");
strcpy(a.InvestorID, "1000001");
strcpy(a.InstrumentID, "rb1809");
m_pUserApi-&gt;ReqQryInstrumentOrderCommRate(&amp;a, 1);
</code></pre>
<span class="anchor" id="9128e076-c521-4f28-b30c-8ee3b8e62c4e"></span>
## 6.FAQ
<p>无</p>
