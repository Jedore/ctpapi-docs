<p>请求投资者商品群SPMM记录查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORCOMMODITYSPMMMARGIN/">OnRspQryInvestorCommoditySPMMMargin</a></p>
<span class="anchor" id="c34d4fb8-7283-4ac4-9cf6-4a4aaf1866c6"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorCommodityGroupSPMMMargin(CThostFtdcQryInvestorCommodityGroupSPMMMarginField *pQryInvestorCommodityGroupSPMMMargin, int nRequestID) = 0;</p>
<span class="anchor" id="78814ee1-254d-493d-a035-8f241905ed72"></span>
## 2.参数
<p>pQryInvestorCommodityGroupSPMMMargin:投资者商品群SPMM记录查询</p>
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
<td style="TEXT-ALIGN: left;">CommodityGroupID</td>
<td style="TEXT-ALIGN: left;">商品群代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="934304a8-fbae-4129-84d9-f4b865d7b1b8"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a380a9ea-892b-4b8c-960a-4e3571a8ad48"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorCommodityGroupSPMMMarginField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.CommodityGroupID, "01");
m_pUserApi-&gt;ReqQryInvestorCommodityGroupSPMMMargin(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="c43efa53-3967-47e5-8065-19d43571c2f5"></span>
## 5.FAQ
<p>无</p>
