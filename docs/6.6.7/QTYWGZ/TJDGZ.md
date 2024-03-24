<span class="anchor" id="7c4c91fb-6658-4214-9b76-a01217c75dc1"></span>
## 1.简介
<p>条件单是一个带有触发条件的指令。该触发条件可以以市场上的最新行情为基准，也可以以指定价格为基准。比如：一个投资者有1手IF1910的空头持仓，并希望在市场价低于2200时买入平仓，他就可以使用条件单。这样当行情波动到满足该条件时，该报单就会被自动触发报出，而不需要他本人时刻盯着电脑屏幕去监视市场行情。</p>
<p>申报条件单时，条件单的报单回报中OrderSysID是以字符串“TJBD_”开头的由CTP系统自定义的报单编号，针对该交易所当日唯一；只对成功申报的条件单编号，错单不编号。因为这种情况下的编号由CTP系统自行维护，与交易所无关，仅用于管理本系统内的该条件单。</p>
<p>有效的使用条件单，可以做出限价止损指令（stop-and-limit order）和触及市价指令（market-if-touched order）。</p>
<p>CTP条件单为CTP后台系统自带指令，并非交易所官方支持指令。</p>
<span class="anchor" id="fb48bbfc-40ec-4a9f-9c7a-f6f872c6a761"></span>
## 2.指令介绍
<p>报入条件单指令使用<a href="../../JYJK/CTHOSTFTDCTRADERSPI/REQORDERINSERT/">ReqOrderInsert</a>函数</p>
<p>其中的核心数据结构是CThostFtdcInputOrderField</p>
<p>在结构体中和普通报单有区别的字段如下：</p>
<pre><code>    ///触发条件
    TThostFtdcContingentConditionType   ContingentCondition;
    ///止损价
    TThostFtdcPriceType StopPrice;
</code></pre>
<p>条件单有效的触发条件如下：</p>
<pre><code>    ///最新价大于条件价
    #define THOST_FTDC_CC_LastPriceGreaterThanStopPrice '5'
    ///最新价大于等于条件价
    #define THOST_FTDC_CC_LastPriceGreaterEqualStopPrice '6'
    ///最新价小于条件价
    #define THOST_FTDC_CC_LastPriceLesserThanStopPrice '7'
    ///最新价小于等于条件价
    #define THOST_FTDC_CC_LastPriceLesserEqualStopPrice '8'
    ///卖一价大于条件价
    #define THOST_FTDC_CC_AskPriceGreaterThanStopPrice '9'
    ///卖一价大于等于条件价
    #define THOST_FTDC_CC_AskPriceGreaterEqualStopPrice 'A'
    ///卖一价小于条件价
    #define THOST_FTDC_CC_AskPriceLesserThanStopPrice 'B'
    ///卖一价小于等于条件价
    #define THOST_FTDC_CC_AskPriceLesserEqualStopPrice 'C'
    ///买一价大于条件价
    #define THOST_FTDC_CC_BidPriceGreaterThanStopPrice 'D'
    ///买一价大于等于条件价
    #define THOST_FTDC_CC_BidPriceGreaterEqualStopPrice 'E'
    ///买一价小于条件价
    #define THOST_FTDC_CC_BidPriceLesserThanStopPrice 'F'
    ///买一价小于等于条件价
    #define THOST_FTDC_CC_BidPriceLesserEqualStopPrice 'H'
</code></pre>
<p>条件价对应的字段为StopPrice</p>
