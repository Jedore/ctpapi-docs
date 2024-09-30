<p>请求SPBM期货合约参数查询响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYSPBMFUTUREPARAMETER/">ReqQrySPBMFutureParameter</a>后，该方法被调用。</p>
<span class="anchor" id="f22b8d19-5bed-43a9-bc5b-c3ee97df10c5"></span>
## 1.函数原型
<p>virtual void OnRspQrySPBMFutureParameter(CThostFtdcSPBMFutureParameterField *pSPBMFutureParameter, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="ae0213d8-8764-46d7-ad4a-eb6729eb2fbe"></span>
## 2.参数
<p>pSPBMFutureParameter：SPBM期货合约保证金参数</p>
<pre><code>struct CThostFtdcSPBMFutureParameterField
{
    ///交易日
    TThostFtdcDateType  TradingDay;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
    ///期货合约因子
    TThostFtdcVolumeMultipleType    Cvf;
    ///阶段标识
    TThostFtdcTimeRangeType TimeRange;
    ///品种保证金标准
    TThostFtdcRatioType MarginRate;
    ///期货合约内部对锁仓费率折扣比例
    TThostFtdcRatioType LockRateX;
    ///提高保证金标准
    TThostFtdcRatioType AddOnRate;
    ///昨结算价
    TThostFtdcPriceType PreSettlementPrice;
    ///期货合约内部对锁仓附加费率折扣比例
    TThostFtdcRatioType AddOnLockRateX2;
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
<span class="anchor" id="7aa3e88f-64cd-411c-9a25-9c4ba4033fb0"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="461d5d01-15c5-4cdd-a043-78fe2ae28ecb"></span>
## 4.FAQ
<p>无</p>
