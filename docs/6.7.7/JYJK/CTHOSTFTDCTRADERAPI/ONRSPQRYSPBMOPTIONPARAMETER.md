<p>请求SPBM期权合约参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMOPTIONPARAMETER/">ReqQrySPBMOptionParameter</a>后，该方法被调用。</p>
<span class="anchor" id="32567516-ef84-4d91-8f78-4b1ceefc150e"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMOptionParameter(CThostFtdcSPBMOptionParameterField *pSPBMOptionParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="494f20fc-ee3c-4973-b4c8-70fb0682f66b"></span>
## 2.参数
<p>pSPBMOptionParameter：SPBM期权合约保证金参数</p>
<pre><code>struct CThostFtdcSPBMOptionParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///期权合约因子
    TThostFtdcVolumeMultipleType    Cvf;
    ///期权冲抵价格
    TThostFtdcPriceType DownPrice;
    ///Delta值
    TThostFtdcDeltaType Delta;
    ///卖方期权风险转换最低值
    TThostFtdcDeltaType SlimiDelta;
    ///昨结算价
    TThostFtdcPriceType PreSettlementPrice;
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
<span class="anchor" id="821dfe03-9171-4a40-b69a-0d2b5d280fd6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5d2dff73-d248-4311-837e-d7fef417e06c"></span>
## 4.FAQ
<p>无</p>
