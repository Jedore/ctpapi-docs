<p>请求SPBM期权合约参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMOPTIONPARAMETER/">ReqQrySPBMOptionParameter</a>后，该方法被调用。</p>
<span class="anchor" id="708b52c9-0e3b-41de-84e9-b9602c2d25a6"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMOptionParameter(CThostFtdcSPBMOptionParameterField *pSPBMOptionParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="504adc6e-a547-433d-a74b-6da4a17f432a"></span>
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
<span class="anchor" id="a215059d-8e8b-4a25-8c03-3833f06aa0a8"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="c27ac91d-8c81-4948-81a9-2e823b5b923e"></span>
## 4.FAQ
<p>无</p>
