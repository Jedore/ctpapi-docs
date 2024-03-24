<p>请求投资者商品群SPMM记录查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORCOMMODITYSPMMMARGIN/">OnRspQryInvestorCommoditySPMMMargin</a></p>
<span class="anchor" id="0c1caf72-55e3-4edd-b5fb-08f72f4cb7d2"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorCommodityGroupSPMMMargin(CThostFtdcQryInvestorCommodityGroupSPMMMarginField *pQryInvestorCommodityGroupSPMMMargin, int nRequestID) = 0;</p>
<span class="anchor" id="b6ba47f7-13ff-4fa2-945a-2904a62f5a61"></span>
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
<span class="anchor" id="da78e42e-d305-4495-8c85-dcb0a0202fd2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="32b1d284-abfe-4996-b23f-45a3d92794b7"></span>
## 4.调用示例
<pre><code>CThostFtdcQryInvestorCommodityGroupSPMMMarginField a = { 0 };
strcpy_s(a.BrokerID, "9999");
strcpy_s(a.InvestorID, "1000001");
strcpy_s(a.CommodityGroupID, "01");
m_pUserApi-&gt;ReqQryInvestorCommodityGroupSPMMMargin(&amp;a, nRequestID++);
</code></pre>
<span class="anchor" id="5a5eae00-c3f8-41f7-ba7b-2a1b2f8e02b9"></span>
## 5.FAQ
<p>无</p>
