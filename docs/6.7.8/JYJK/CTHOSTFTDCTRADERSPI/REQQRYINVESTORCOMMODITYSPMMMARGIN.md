<p>请求投资者商品组SPMM记录查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORCOMMODITYSPMMMARGIN/">OnRspQryInvestorCommoditySPMMMargin</a></p>
<span class="anchor" id="e57e6a00-8200-43a9-8b66-f90aa767765f"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorCommoditySPMMMargin(CThostFtdcQryInvestorCommoditySPMMMarginField *pQryInvestorCommoditySPMMMargin, int nRequestID) = 0;</p>
<span class="anchor" id="0f5e765f-4469-4f64-89a8-81a6cbf218ac"></span>
## 2.参数
<p>pQryInvestorCommoditySPMMMargin：投资者商品组SPMM记录查询</p>
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
<tr><td style="TEXT-ALIGN: left;">TThostFtdcSPMMProductIDType</td>
<td style="TEXT-ALIGN: left;">CommodityID</td>
<td style="TEXT-ALIGN: left;">商品组代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="14a6439c-8724-4708-8bc8-3dcdb477f8b0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="0b0d3607-4037-41e2-9ca1-736b3cf2b405"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorCommoditySPMMMarginField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.CommodityID, "cu&amp;cu_o");
m_pUserApi-&gt;ReqQryInvestorCommoditySPMMMargin(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="37758ab8-8ba2-4574-91fb-ad3fc41700cf"></span>
## 5.FAQ
<p>无</p>
