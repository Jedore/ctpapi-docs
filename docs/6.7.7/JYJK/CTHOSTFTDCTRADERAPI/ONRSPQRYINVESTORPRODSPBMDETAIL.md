<p>请求投资者产品SPBM明细查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYINVESTORPRODSPBMDETAIL/">ReqQryInvestorProdSPBMDetail</a>后，该方法被调用。</p>
<span class="anchor" id="2534f9d2-bf91-4fce-9640-431e7f094284"></span>
## 1.函数原型
<p>virtual void OnRspQryInvestorProdSPBMDetail(CThostFtdcInvestorProdSPBMDetailField *pInvestorProdSPBMDetail, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="906e86cf-8549-4053-aba4-5d27b564be32"></span>
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
<span class="anchor" id="6f3bb617-1fd6-4d2c-82b3-a25e6ddcad17"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a2937efe-6a63-408c-9d59-8887c90476d0"></span>
## 4.FAQ
<p>无</p>
