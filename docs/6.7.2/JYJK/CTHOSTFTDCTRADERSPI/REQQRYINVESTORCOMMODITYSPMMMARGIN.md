<p>请求投资者商品组SPMM记录查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORCOMMODITYSPMMMARGIN/">OnRspQryInvestorCommoditySPMMMargin</a></p>
<span class="anchor" id="d001ebc1-f1cf-4103-b8fd-a4381635c8f2"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorCommoditySPMMMargin(CThostFtdcQryInvestorCommoditySPMMMarginField *pQryInvestorCommoditySPMMMargin, int nRequestID) = 0;</p>
<span class="anchor" id="351f8084-ed59-44f6-8daf-b1e693dd4cb9"></span>
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
<span class="anchor" id="ddec9c9f-be07-4840-9d80-39d752af1a05"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d65c34ff-4fdc-4166-9356-77a2808f7201"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorCommoditySPMMMarginField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.CommodityID, "cu&amp;cu_o");
m_pUserApi-&gt;ReqQryInvestorCommoditySPMMMargin(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="2ca5f6ff-cdc1-48a6-9768-6788a09a0e9c"></span>
## 5.FAQ
<p>无</p>
