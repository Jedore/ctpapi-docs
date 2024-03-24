<p>请求SPBM期权合约参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMOPTIONPARAMETER/">ReqQrySPBMOptionParameter</a>后，该方法被调用。</p>
<span class="anchor" id="cb5edfdb-5086-49e5-9faf-c029e5f9209d"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMOptionParameter(CThostFtdcSPBMOptionParameterField *pSPBMOptionParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="2f31fc32-3871-47e2-87e8-7f216a9c9400"></span>
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
<span class="anchor" id="d9e6fb39-d684-4393-abe8-4c72463b5cb9"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5f798d7a-af73-4562-9a87-8833ee83b5d0"></span>
## 4.FAQ
<p>无</p>
