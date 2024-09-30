<p>请求投资者新型组合保证金系数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFMARGINRATIO/">ReqQryInvestorPortfMarginRatio</a>后，该方法被调用。</p>
<span class="anchor" id="e9cd7f5e-cea8-4885-81eb-344820bf4838"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPortfMarginRatio(CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="8d8bf4be-e027-41cf-9d19-93d966e796ee"></span>
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
<span class="anchor" id="6bf0206d-2d35-4d9a-ac08-1f4fbcb32f1d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="f6fd50e0-5eeb-4c60-ade0-5c7240b04a1b"></span>
## 4.FAQ
<p>无</p>
