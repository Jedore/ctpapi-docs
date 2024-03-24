<p>请求查询产品</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYPRODUCT/">OnRspQryProduct</a></p>
<span class="anchor" id="1dda4a5a-2ae7-4669-b12d-63bf5578b4a1"></span>
## 1.函数原型
<p>virtual int ReqQryProduct(CThostFtdcQryProductField *pQryProduct, int nRequestID) = 0;</p>
<span class="anchor" id="840cb02b-cda5-4dc5-85fe-9f0b46c1ae57"></span>
## 2.参数
<p>pQryProduct：查询产品</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">产品类型</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcProductClassType</td>
<td style="TEXT-ALIGN: left;">ProductClass</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="3a4418fa-eb5a-47a2-ac5b-4ef3492e0f83"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6f352952-0ce0-4bfa-891c-72cb9ae7fdb7"></span>
## 4.调用示例
<pre><code>CThostFtdcQryProductField a = { 0 };
strcpy_s(a.ProductID, "sc");
a.ProductClass = THOST_FTDC_PC_Futures;
strcpy_s(a.ExchangeID, "SHFE");
m_pUserApi-&gt;ReqQryProduct(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="bf011391-558a-4c9b-a66d-23c6b18e95db"></span>
## 5.FAQ
<p>无</p>
