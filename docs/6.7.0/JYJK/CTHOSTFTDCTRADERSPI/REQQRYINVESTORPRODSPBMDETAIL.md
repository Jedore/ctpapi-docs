<p>请求投资者产品SPBM明细查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYINVESTORPRODSPBMDETAIL/">OnRspQryInvestorProdSPBMDetail</a></p>
<span class="anchor" id="8851ed02-d708-4801-adbc-1de870e16d09"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorProdSPBMDetail(CThostFtdcQryInvestorProdSPBMDetailField *pQryInvestorProdSPBMDetail, int nRequestID) = 0;</p>
<span class="anchor" id="b2e10ebd-b588-48a1-b740-568ddf35e039"></span>
## 2.参数
<p>pQryInvestorProdSPBMDetail：投资者产品SPBM明细查询</p>
<pre><code>struct CThostFtdcQryInvestorProdSPBMDetailField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
};
</code></pre>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">投资者代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInvestorIDType</td>
<td style="TEXT-ALIGN: left;">InvestorID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="2e6f2287-5c24-4ba1-8ea0-97b03880a2da"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8df46dc3-4c75-4dd2-8f51-0e2f22e7c82b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="24a195e3-0d41-4bb7-a927-6b88a6a63cbf"></span>
## 5.FAQ
<p>无</p>
