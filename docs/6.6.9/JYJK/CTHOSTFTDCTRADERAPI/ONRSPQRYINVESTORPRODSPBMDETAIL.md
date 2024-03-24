<p>请求投资者产品SPBM明细查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODSPBMDETAIL/">ReqQryInvestorProdSPBMDetail</a>后，该方法被调用。</p>
<span class="anchor" id="7d5d6068-4100-466e-8748-b371af22b35f"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorProdSPBMDetail(CThostFtdcInvestorProdSPBMDetailField *pInvestorProdSPBMDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="5f479d5f-b4d7-43c9-9d4a-88d1b275d6d3"></span>
## 2.参数
<p>pInvestorProdSPBMDetail：投资者产品SPBM明细</p>
<pre><code>struct CThostFtdcInvestorProdSPBMDetailField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///合约内对锁保证金
    TThostFtdcMoneyType IntraInstrMargin;
    ///买归集保证金
    TThostFtdcMoneyType BCollectingMargin;
    ///卖归集保证金
    TThostFtdcMoneyType SCollectingMargin;
    ///品种内合约间对锁保证金
    TThostFtdcMoneyType IntraProdMargin;
    ///净保证金
    TThostFtdcMoneyType NetMargin;
    ///产品间对锁保证金
    TThostFtdcMoneyType InterProdMargin;
    ///裸保证金
    TThostFtdcMoneyType SingleMargin;
    ///附加保证金
    TThostFtdcMoneyType AddOnMargin;
    ///交割月保证金
    TThostFtdcMoneyType DeliveryMargin;
    ///看涨期权最低风险
    TThostFtdcMoneyType CallOptionMinRisk;
    ///看跌期权最低风险
    TThostFtdcMoneyType PutOptionMinRisk;
    ///卖方期权最低风险
    TThostFtdcMoneyType OptionMinRisk;
    ///买方期权冲抵价值
    TThostFtdcMoneyType OptionValueOffset;
    ///卖方期权权利金
    TThostFtdcMoneyType OptionRoyalty;
    ///价值冲抵
    TThostFtdcMoneyType RealOptionValueOffset;
    ///保证金
    TThostFtdcMoneyType Margin;
    ///交易所保证金
    TThostFtdcMoneyType ExchMargin;
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
<span class="anchor" id="57ccd88c-f3ea-4f56-b602-5993a848f23a"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="22e7a00a-80fb-4743-a4dc-c3640a459800"></span>
## 4.FAQ
<p>无</p>
