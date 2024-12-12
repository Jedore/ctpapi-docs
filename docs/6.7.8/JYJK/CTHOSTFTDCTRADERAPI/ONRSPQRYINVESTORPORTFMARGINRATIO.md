<p>请求投资者新型组合保证金系数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFMARGINRATIO/">ReqQryInvestorPortfMarginRatio</a>后，该方法被调用。</p>
<span class="anchor" id="d1f5c8f8-dcf5-4bb4-aa71-9805e004c783"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPortfMarginRatio(CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="d3793785-e324-4b74-96d2-244f89226511"></span>
## 2.参数
<p>pInvestorPortfMarginRatio：投资者新型组合保证金系数</p>
<pre><code>struct CThostFtdcInvestorPortfMarginRatioField
{
    ///投资者范围
    TThostFtdcInvestorRangeType InvestorRange;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///会员对投资者收取的保证金和交易所对投资者收取的保证金的比例
    TThostFtdcRatioType MarginRatio;
    ///产品群代码
    TThostFtdcProductIDType ProductGroupID;
};
</code></pre>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="fa5f34a0-0be8-4998-8adc-417cbe8aa282"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="67b84905-36e6-41f9-9e00-83717988f565"></span>
## 4.FAQ
<p>无</p>
