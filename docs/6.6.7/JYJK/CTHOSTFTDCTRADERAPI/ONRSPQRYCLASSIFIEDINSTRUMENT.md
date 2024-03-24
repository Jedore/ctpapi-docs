<p>请求查询分类合约响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYCLASSIFIEDINSTRUMENT/">ReqQryClassifiedInstrument</a>后，该方法被调用。</p>
<span class="anchor" id="51bd2bce-8ae6-4ef1-bf1d-679510fa97ae"></span>
## 1.函数原型
<p>virtual void OnRspQryClassifiedInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="a078db2d-343f-41c3-bf25-a7477e7fb224"></span>
## 2.参数
<p>pInstrument：合约</p>
<pre><code>struct CThostFtdcInstrumentField
{
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///合约名称
    TThostFtdcInstrumentNameType    InstrumentName;
    ///保留的无效字段
    TThostFtdcOldExchangeInstIDType reserve2;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve3;
    ///产品类型
    TThostFtdcProductClassType  ProductClass;
    ///交割年份
    TThostFtdcYearType  DeliveryYear;
    ///交割月
    TThostFtdcMonthType DeliveryMonth;
    ///市价单最大下单量
    TThostFtdcVolumeType    MaxMarketOrderVolume;
    ///市价单最小下单量
    TThostFtdcVolumeType    MinMarketOrderVolume;
    ///限价单最大下单量
    TThostFtdcVolumeType    MaxLimitOrderVolume;
    ///限价单最小下单量
    TThostFtdcVolumeType    MinLimitOrderVolume;
    ///合约数量乘数
    TThostFtdcVolumeMultipleType    VolumeMultiple;
    ///最小变动价位
    TThostFtdcPriceType PriceTick;
    ///创建日
    TThostFtdcDateType  CreateDate;
    ///上市日
    TThostFtdcDateType  OpenDate;
    ///到期日
    TThostFtdcDateType  ExpireDate;
    ///开始交割日
    TThostFtdcDateType  StartDelivDate;
    ///结束交割日
    TThostFtdcDateType  EndDelivDate;
    ///合约生命周期状态
    TThostFtdcInstLifePhaseType InstLifePhase;
    ///当前是否交易
    TThostFtdcBoolType  IsTrading;
    ///持仓类型
    TThostFtdcPositionTypeType  PositionType;
    ///持仓日期类型
    TThostFtdcPositionDateTypeType  PositionDateType;
    ///多头保证金率
    TThostFtdcRatioType LongMarginRatio;
    ///空头保证金率
    TThostFtdcRatioType ShortMarginRatio;
    ///是否使用大额单边保证金算法
    TThostFtdcMaxMarginSideAlgorithmType    MaxMarginSideAlgorithm;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve4;
    ///执行价
    TThostFtdcPriceType StrikePrice;
    ///期权类型
    TThostFtdcOptionsTypeType   OptionsType;
    ///合约基础商品乘数
    TThostFtdcUnderlyingMultipleType    UnderlyingMultiple;
    ///组合类型
    TThostFtdcCombinationTypeType   CombinationType;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///合约在交易所的代码
    TThostFtdcExchangeInstIDType    ExchangeInstID;
    ///产品代码
    TThostFtdcInstrumentIDType  ProductID;
    ///基础商品代码
    TThostFtdcInstrumentIDType  UnderlyingInstrID;
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
<span class="anchor" id="e00a4151-e863-496a-b818-b581e42837dd"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="26d1c3a5-0380-4bb9-86aa-d1f04516ba51"></span>
## 4.FAQ
<p>无</p>
