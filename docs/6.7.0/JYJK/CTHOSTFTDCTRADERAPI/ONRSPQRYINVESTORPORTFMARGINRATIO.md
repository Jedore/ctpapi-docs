<p>请求投资者新型组合保证金系数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPORTFMARGINRATIO/">ReqQryInvestorPortfMarginRatio</a>后，该方法被调用。</p>
<span class="anchor" id="4f2bd059-e10a-4ca8-b006-4df8f3c9a456"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorPortfMarginRatio(CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="680b95e1-84e7-4d66-8d33-07a09e8bcedf"></span>
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
<span class="anchor" id="855e0bb7-815d-4e6a-966e-4a2576c7e12a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ec8688a6-a1eb-4f67-a036-7356cd9160f6"></span>
## 4.FAQ
<p>无</p>
